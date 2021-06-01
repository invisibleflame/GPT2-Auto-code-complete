from github import Github
import time
from datetime import datetime

ACCESS_TOKEN = ""
g = Github(ACCESS_TOKEN)

end_time= time.time()
start_time= end_time - 86400


for i in range(10):
	start_time_str = datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d")
	end_time_str = datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d")
	query = f"language:python created:{start_time_str}..{end_time_str}"
	end_time-=86400
	start_time-=86400
	result = g.search_repositories(query)

	for repositry in result:
		os.system(f"git clone {repositry.clone_url} data/{repository.owner.login}/{repository.name}")
