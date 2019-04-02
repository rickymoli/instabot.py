from datetime import datetime, timedelta
from followers_consolidation import FollowersConsolidation
from news_vs_recurrents_consolidation import NewsVsRecurrentsConsolidation
from add_interactions_consolidation import AddInteractionsConsolidation

followers_consolidation = FollowersConsolidation()
news_vs_recurrents_consolidation = NewsVsRecurrentsConsolidation()
add_interactions_consolidation = AddInteractionsConsolidation()

yesterday = datetime.now() - timedelta(days=1)
yesterday_start = datetime(yesterday.year, yesterday.month, yesterday.day)
yesterday_end = yesterday_start + timedelta(1)

followers_consolidation.execute(yesterday_start,yesterday_end)
# news_vs_recurrents_consolidation.execute(yesterday_start,yesterday_end)
add_interactions_consolidation.execute(yesterday_start, yesterday_end)
