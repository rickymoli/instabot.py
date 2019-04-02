% rebase('base.tpl',title='Growth of followers',followers_growth=followers_growth)
<div class="row">
  <div class="col">
    <canvas id="growthFollowersChart" width="100%" height="30px"></canvas>
  </div>
</div>
<div class="row">
  <div class="col">
    <!-- <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3">
      <h5>By tags</h5>
      <div class="btn-toolbar mb-2 mb-md-0">
        <div class="dropdown">
          <button class="btn btn-outline-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Last day
          </button>
          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <a class="dropdown-item" href="#">Last day</a>
            <a class="dropdown-item" href="#">Last 3 days</a>
            <a class="dropdown-item" href="#">Last 7 days</a>
          </div>
        </div>
      </div>
    </div> -->
    <br /><br />
    <div class="row">
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th>Best tags</th>
              <th class="text-right">Growth</th>
              <th class="text-right">Accurate</th>
            </tr>
          </thead>
          <tbody>
            % for tag in best_tags:
            <tr>
              <td>{{tag['_id']}}</td>
              <td class="text-right">{{tag['growth']}}</td>
              <td class="text-right">{{round(tag['accurate'],2)}}%</td>
            </tr>
            % end
          </tbody>
        </table>
      </div>
      <div class="col">
        <table class="table">
          <thead>
            <tr>
              <th>Worst tags</th>
              <th class="text-right">Interactions</th>
            </tr>
          </thead>
          <tbody>
            % for tag in worst_tags:
            <tr>
              <td>{{tag['_id']}}</td>
              <td class="text-right">{{tag['interactions']}}</td>
            </tr>
            % end
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
