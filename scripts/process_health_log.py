import re
import pathlib

RAW_DIR = pathlib.Path("current/health-log/raw")
OUT_DIR = pathlib.Path("current/health-log")

# Целевые диапазоны фаз сна (% от общего сна), по научной литературе:
# Deep (N3): 13-23% (Sleep Foundation / Medscape), центр ~18%
# REM: 20-25% (стандартный диапазон для взрослых), центр ~22.5%
# Целевая длительность сна: 7ч = 420 мин
DEEP_TARGET_CENTER = 18.0
DEEP_TARGET_RANGE = 5.0  # 13-23% -> +/-5 от центра 18
REM_TARGET_CENTER = 22.5
REM_TARGET_RANGE = 2.5  # 20-25% -> +/-2.5 от центра 22.5
DURATION_TARGET_MIN = 420  # 7 часов


def parse_num(s: str) -> float:
    """Handle both comma and dot as decimal separator (device locale may use comma)."""
    return float(s.replace(",", "."))


def closeness_score(actual: float, center: float, half_range: float) -> float:
    """100 если actual == center, линейно падает до 0 на расстоянии >= half_range*2
    (т.е. штрафуем и за недобор, и за перебор относительно целевого диапазона)."""
    deviation = abs(actual - center)
    return max(0.0, 100.0 - (deviation / (half_range * 2)) * 100.0)


def process_file(raw_path: pathlib.Path) -> None:
    text = raw_path.read_text(encoding="utf-8")

    values = {}
    for key in ("Steps", "Core", "Deep", "REM", "Awake"):
        m = re.search(rf"{key}\s+([\d.,]+)", text)
        if m:
            values[key] = parse_num(m.group(1))

    core_sec = values.get("Core", 0.0)
    deep_sec = values.get("Deep", 0.0)
    rem_sec = values.get("REM", 0.0)
    steps = values.get("Steps")

    core_min = round(core_sec / 60)
    deep_min = round(deep_sec / 60)
    rem_min = round(rem_sec / 60)
    total_min = core_min + deep_min + rem_min

    score = None
    deep_pct = rem_pct = None
    if total_min > 0:
        deep_pct = deep_min / total_min * 100
        rem_pct = rem_min / total_min * 100

        deep_score = closeness_score(deep_pct, DEEP_TARGET_CENTER, DEEP_TARGET_RANGE)
        rem_score = closeness_score(rem_pct, REM_TARGET_CENTER, REM_TARGET_RANGE)
        duration_score = min(total_min / DURATION_TARGET_MIN, 1.0) * 100.0

        score = round((deep_score + rem_score + duration_score) / 3)

    hours, minutes = divmod(total_min, 60)

    date_str = raw_path.stem  # expects raw/YYYY-MM-DD.md

    lines = [f"# Health log — {date_str}", ""]
    if steps is not None:
        lines.append(f"Шаги: {round(steps)}")
    lines.append(
        f"Сон: {hours} ч {minutes} мин "
        f"(Core {core_min} мин, Deep {deep_min} мин, REM {rem_min} мин)"
    )
    if score is not None:
        lines.append(
            f"Sleep score ({score}/100): среднее из трёх компонент - "
            f"близость доли Deep к норме 13-23% (сейчас {deep_pct:.0f}%), "
            f"близость доли REM к норме 20-25% (сейчас {rem_pct:.0f}%), "
            f"длительность сна к цели 7ч"
        )

    out_path = OUT_DIR / f"{date_str}.md"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Processed {raw_path} -> {out_path}")


def main() -> None:
    if not RAW_DIR.exists():
        print("No raw dir, nothing to do")
        return
    for raw_path in sorted(RAW_DIR.glob("*.md")):
        process_file(raw_path)


if __name__ == "__main__":
    main()
