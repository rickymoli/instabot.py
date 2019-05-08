from datetime import datetime, timedelta
from followers_consolidation import FollowersConsolidation
from news_vs_recurrents_consolidation import NewsVsRecurrentsConsolidation
from add_interactions_consolidation import AddInteractionsConsolidation

followers_consolidation = FollowersConsolidation()
news_vs_recurrents_consolidation = NewsVsRecurrentsConsolidation()
add_interactions_consolidation = AddInteractionsConsolidation()

param_start = datetime(2019, 3, 29)
param_end = datetime(2019, 3, 29)
start = param_start
end = start + timedelta(1)
while start <= param_end:
    followers_consolidation.execute(start, end)
    # news_vs_recurrents_consolidation.execute(start, end)
    add_interactions_consolidation.execute(start, end)
    print(start)
    start = end
    end = start + timedelta(1)
