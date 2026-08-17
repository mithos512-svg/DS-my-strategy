# Команда: "График веса" (ключевое слово)

> Вызывается из ЛЮБОГО чата фразой "График веса" (или близким по смыслу
> запросом на визуализацию динамики веса). Не требует поднимать остальной
> контекст сессии - самодостаточная команда.

## Что делать при вызове

1. Прочитать **весь** `current/weight-log.md` заново (не полагаться на
   память/индекс - файл обновляется каждый Day Close, данные должны быть
   свежими).
2. Собрать три ряда:
   - **Daily Weight** - каждая строка лога (дата → вес).
   - **Weekly Average Weight** - среднее по календарным неделям
     понедельник-воскресенье, точка ставится на последний день недели.
     Пропуски измерений в неделе не портят среднее (просто меньше слагаемых).
     Метка недели (W28, W29...) не показывается на графике, только внутри
     данных для справки.
   - **Body Fat % (US Navy)** - только те даты, где в weight-log.md явно
     указан % жира (обычно раз в 1-2 недели вместе с замером талии/шеи).
3. **Сегодняшний день в график НЕ включать** (правило от 17.08.2026 - по
   умолчанию график показывает только завершённые дни; если пользователь
   явно попросит включить сегодня - включить).
4. Сгенерировать HTML-файл по шаблону ниже, подставив свежие данные вместо
   трёх констант (`dailyLabels`, `dailyWeight`, `weeklyAvgPoints`,
   `bodyFatPoints`), сохранить в `/mnt/user-data/outputs/`, вызвать
   `present_files`.
5. **Все подписи на графике - только по-английски** (правило от 17.08.2026).
6. Зоны body fat % (US Navy, для мужчины) фиксированные, не пересчитывать:
   - Obese: 25%+
   - Normal: 14-24%
   - Athletic / Pro: <14%
   Подписи зон - справа, у самой оси Body Fat % (`position: {x:'end', ...}`)
   - так было явно запрошено 17.08.2026.

## HTML-шаблон (рабочая версия на 17.08.2026)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Weight & Body Fat Trend</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-annotation/3.0.1/chartjs-plugin-annotation.min.js"></script>
<style>
  html, body {
    margin: 0;
    padding: 0;
    background: #faf8f5;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  }
  .wrap {
    max-width: 980px;
    margin: 0 auto;
    padding: 24px 20px 32px;
  }
  h1 {
    font-size: 20px;
    font-weight: 600;
    color: #2b2b28;
    margin: 0 0 4px;
  }
  .subtitle {
    font-size: 13px;
    color: #8a8478;
    margin: 0 0 20px;
  }
  .chart-box {
    background: #ffffff;
    border-radius: 12px;
    padding: 20px 16px 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }
  canvas { max-height: 480px; }
</style>
</head>
<body>
<div class="wrap">
  <h1>Weight &amp; Body Fat Trend</h1>
  <p class="subtitle">Daily weight, weekly average, and body fat % · &lt;DATE RANGE&gt;</p>
  <div class="chart-box">
    <canvas id="chart"></canvas>
  </div>
</div>

<script>
// === REPLACE THESE 4 CONSTANTS WITH FRESH DATA FROM current/weight-log.md ===
const dailyLabels = [/* "MM-DD", ... , exclude today */];
const dailyWeight = [/* matching weight values */];
const weeklyAvgPoints = [/* {x:"MM-DD" (=last day of week), y: avg, week:"WNN"}, ... */];
const bodyFatPoints = [/* {x:"MM-DD", y: bodyFat%}, ... only dates with a measurement */];
// === END REPLACE ===

function toSparseSeries(points) {
  return dailyLabels.map(lbl => {
    const p = points.find(pt => pt.x === lbl);
    return p ? p.y : null;
  });
}

const weeklyAvgSeries = toSparseSeries(weeklyAvgPoints);
const bodyFatSeries = toSparseSeries(bodyFatPoints);

if (window.ChartAnnotation) { Chart.register(window.ChartAnnotation); }

const ctx = document.getElementById('chart').getContext('2d');
new Chart(ctx, {
  type: 'line',
  data: {
    labels: dailyLabels,
    datasets: [
      {
        label: 'Daily Weight (kg)',
        data: dailyWeight,
        borderColor: '#b8c4a8',
        backgroundColor: '#b8c4a8',
        borderWidth: 1.5,
        pointRadius: 2,
        tension: 0.25,
        yAxisID: 'yWeight',
        spanGaps: true
      },
      {
        label: 'Weekly Average Weight (kg)',
        data: weeklyAvgSeries,
        borderColor: '#8a6d5c',
        backgroundColor: '#8a6d5c',
        borderWidth: 3,
        pointRadius: 5,
        pointStyle: 'rectRot',
        tension: 0,
        spanGaps: true,
        yAxisID: 'yWeight'
      },
      {
        label: 'Body Fat % (US Navy)',
        data: bodyFatSeries,
        borderColor: '#c76b5f',
        backgroundColor: '#c76b5f',
        borderWidth: 2,
        borderDash: [4,3],
        pointRadius: 5,
        pointStyle: 'triangle',
        tension: 0,
        spanGaps: true,
        yAxisID: 'yFat'
      }
    ]
  },
  options: {
    responsive: true,
    interaction: { mode: 'index', intersect: false },
    plugins: {
      legend: {
        position: 'top',
        labels: { usePointStyle: true, boxWidth: 8, font: { size: 12 } }
      },
      tooltip: { backgroundColor: '#2b2b28' },
      annotation: {
        annotations: {
          zoneObese: {
            type: 'box',
            yScaleID: 'yFat',
            yMin: 25,
            yMax: 28,
            backgroundColor: 'rgba(199,107,95,0.10)',
            borderWidth: 0,
            label: {
              display: true,
              content: 'Obese (25%+)',
              position: { x: 'end', y: 'start' },
              color: '#c76b5f',
              font: { size: 10, weight: '600' },
              backgroundColor: 'transparent'
            }
          },
          zoneNormal: {
            type: 'box',
            yScaleID: 'yFat',
            yMin: 14,
            yMax: 25,
            backgroundColor: 'rgba(184,196,168,0.14)',
            borderWidth: 0,
            label: {
              display: true,
              content: 'Normal (14–24%)',
              position: { x: 'end', y: 'start' },
              color: '#7c8a68',
              font: { size: 10, weight: '600' },
              backgroundColor: 'transparent'
            }
          },
          zoneAthletic: {
            type: 'box',
            yScaleID: 'yFat',
            yMin: 11,
            yMax: 14,
            backgroundColor: 'rgba(122,150,168,0.14)',
            borderWidth: 0,
            label: {
              display: true,
              content: 'Athletic / Pro (<14%)',
              position: { x: 'end', y: 'end' },
              color: '#5c7d8a',
              font: { size: 10, weight: '600' },
              backgroundColor: 'transparent'
            }
          }
        }
      }
    },
    scales: {
      x: {
        title: { display: true, text: 'Date (MM-DD)', font: { size: 12 } },
        ticks: { maxRotation: 90, minRotation: 90, autoSkip: true, maxTicksLimit: 24, font: { size: 10 } },
        grid: { display: false }
      },
      yWeight: {
        type: 'linear',
        position: 'left',
        title: { display: true, text: 'Weight (kg)', font: { size: 12 } },
        suggestedMin: 80,
        suggestedMax: 88
      },
      yFat: {
        type: 'linear',
        position: 'right',
        title: { display: true, text: 'Body Fat (%)', font: { size: 12 } },
        min: 11,
        max: 28,
        grid: { drawOnChartArea: false }
      }
    }
  }
});
</script>
</body>
</html>
```

> Примечание: `yWeight` диапазон (`suggestedMin`/`suggestedMax` 80/88) и `yFat`
> диапазон (`min`/`max` 11/28) подобраны под данные июля-августа 2026. Если
> вес выйдет за пределы 80-88 или % жира за 11-28, расширить диапазон под
> актуальные данные, иначе точки обрежутся графиком.

---
Создан: 2026-08-17.
