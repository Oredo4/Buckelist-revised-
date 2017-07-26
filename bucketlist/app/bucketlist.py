class Bucketlist(object):
    allbucketlists = []

    def __init__(self, name=None):
        self.name = name

    def create_bucketlist(self, name):
        self.allbucketlists.append(name)
        return 'success'

    def view_bucketlist(self):
        if self.allbucketlists:
            return self.allbucketlists