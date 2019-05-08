<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Reports</title>
  <link rel="stylesheet" href="/bootstrap/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="/chart.js/dist/Chart.min.css">
</head>
<body>
  <!-- <header>
    <div class="navbar navbar-dark bg-dark shadow-sm">
      <div class="container d-flex justify-content-between">
        <a href="#" class="navbar-brand d-flex align-items-center">
          <strong>Reports</strong>
        </a>
      </div>
    </div>
  </header> -->
  <main role="main" class="container">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h3 class="h3">{{title}}</h3>
    </div>
    <div class="container">
      {{!base}}
    </div>
  </main>
  <script src="/jquery/dist/jquery.min.js"></script>
  <script src="/popper.js/dist/umd/popper.min.js"></script>
  <script src="/bootstrap/dist/js/bootstrap.min.js"></script>
  <script src="/chart.js/dist/Chart.min.js"></script>
  <script>
  $(function(){
    var ctx = document.getElementById('growthFollowersChart').getContext('2d');
    var growthFollowersChart = new Chart(ctx, {
      type: 'line',
      options: {
        scales: {
          xAxes: [{
              gridLines: {
                  display:false
              }
          }],
          yAxes: [{
              gridLines: {
                  display:false
              }
          }]
        }
      },
      data: {
        labels: [
          %for followers in followers_growth:
            '{{followers['date']}}',
          %end
        ],
        datasets: [
          {
            label: 'Total',
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            data: [
              %for followers in followers_growth:
                '{{followers['growth']}}',
              %end
            ]
          },
          {
            label: 'Medias',
            fill: false,
            borderColor: 'rgb(192, 75, 192)',
            data: [
              %for followers in followers_growth:
                '{{followers['growth_medias']}}',
              %end
            ]
          },
          {
            label: 'Tags',
            fill: false,
            borderColor: 'rgb(192, 192, 75)',
            data: [
              %for followers in followers_growth:
                '{{followers['growth_tags']}}',
              %end
            ]
          }
        ]
      }
    });
  });
  </script>
</body>
</html>
