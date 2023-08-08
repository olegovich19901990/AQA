class RepositoriesProvider:

    @staticmethod
    def existing_repository():
        return {
            "name": 'my_project',
            "total_count": 1,
        }

    @staticmethod
    def non_existing_repository():
        return {
            "name": 'asljkfgherufjdbv',
            "total_count": 0,
        }