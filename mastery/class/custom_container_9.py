class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, value):
        self.tags[tag.lower()] = value

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

print(cloud.tags["python"])
cloud["java"] = 10
print(cloud.tags)

print(cloud.__len__())

