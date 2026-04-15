<!DOCTYPE html>
<html lang="en">
  <head>
    <title>OpenStreetMap</title>
<!-- ___________________________ Metatags __________________________ -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="author" content="Rockdukan" />
    <meta name="description" content="Информация о городах">
    <meta name="viewport" content="initial-scale=1.0, width=device-width">
<!-- _____________________________ CSS _____________________________ -->
    <link rel="stylesheet" href="/static/css/style.css">
<!-- ______________________ If Internet Explorer ___________________ -->
    <script>
        if (/Trident\/|MSIE/.test(window.navigator.userAgent)) {
            alert("Ваш браузер не поддерживается!!!");
        }
    </script>
  </head>
  <body>
    <div id="wrapper">
<!-- ______________________________ CONTENT ________________________ -->
      <main class="container">
        <div class="content">
          <section class="section">
            <div class="map">
              {{! map }}
            </div>
          </section>
          <section class="section">
            <div class="charts">
              <canvas id="myChart"></canvas>
            </div>
          </section>
          <section class="section">
            <table class="table">
              <thead>
                <tr>
                  <th>Город</th>
                  % for category, tag_dict in tags.items():
                    % for tag_key, tag_name in tag_dict.items():
                      <th>{{tag_name}}</th>
                    % end
                  % end
                </tr>
              </thead>
              <tbody>
                % for city_name_ru, city_tags in city_data.items():
                  <tr>
                    <td>{{city_name_ru}}</td>
                    % for category, tag_dict in tags.items():
                      % for tag_key, tag_name in tag_dict.items():
                        % count = len(city_tags.get(category, {}).get(tag_key, []))
                        <td>{{count}}</td>
                      % end
                    % end
                  </tr>
                % end
              </tbody>
            </table>
          </section>
        </div>
      </main>
<!-- ____________________________ END_CONTENT ______________________ -->
    </div>
<!-- ____________________________ JavaScript _______________________ -->
    <script src="/static/js/chart.js"></script>
    <script>
  const ctx = document.getElementById('myChart');
  const colorPalette = [
    "#4BC0C0", "#FF9F40", "#9966FF", "#36A2EB",
    "#FF6384", "#8BC34A", "#CDDC39", "#FFEB3B",
    "#FF9800", "#795548", "#607D8B", "#00BCD4"
  ];
  var colors = new Map();
  const cityNames = [
    % for name in city_data:
      '{{name}}',
    % end
  ];

  cityNames.forEach((name, index) => {
    colors.set(name, colorPalette[index % colorPalette.length]);
  });

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: [
        % for category, tag_dict in tags.items():
          % for tag, label in tag_dict.items():
            '{{label}}',
          % end
        % end
      ],
      datasets: [
      %for key in city_data:
      {
        borderWidth: 1,
        label: '{{key}}',
        data: [
          % for category, tag_dict in tags.items():
            % for tag in tag_dict:
              {{len(city_data[key].get(category, {}).get(tag, []))}},
            % end
          % end
        ],
        borderColor: colors.get('{{key}}'),
        backgroundColor: colors.get('{{key}}'),
      },
      %end
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        scales: {
          y: {
            beginAtZero: true
          }
        },
        title: {
          display: true,
          text: 'Сравнительный график'
        }
      }
    }
  });
</script>
  </body>
</html>