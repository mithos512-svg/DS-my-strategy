import re
import pathlib

RAW_DIR = pathlib.Path("current/health-log/raw")
OUT_DIR = pathlib.Path("current/health-log")


def parse_num(s: str) -> float:
    """Handle both comma and dot as decimal separator (device locale may use comma)."""
    return float(s.replace(",", "."))


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
    if total_min > 0:
        weighted = deep_min * 2 + rem_min * 1.5 + core_min * 1
        # Normalize against the max possible weighted value (all minutes = Deep, weight 2)
        # so the score is properly bounded 0-100: Core-only -> 50, REM-only -> 75, Deep-only -> 100
        score = round(weighted / (total_min * 2) * 100)

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
        lines.append(f"Sleep score (эвристика Deep×2 + REM×1.5 + Core×1): {score}/100")

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
