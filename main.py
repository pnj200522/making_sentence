from databases.service import DatabaseService as ds

# DatabaseService 인스턴스 생성
database_service = ds("/workspaces/making_sentence/content/mysql_talktree_dev.json")

# get_engine 메서드 호출
engine = database_service.get_engine()
