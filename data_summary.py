# Yuval Berghaus - 313247116
# github - https://github.com/yuvalBerghaus/Data_science
import csv
import json


class DataSummary:
    _dataFile = None
    _metaFile = None
    _features = None

    def sum(self, feature):
        self.check_if_number(feature, "sum")
        sum = 0
        for obj in self._dataFile:
            if obj[feature] is not None:
                sum += float(obj[feature])
        return sum

    def count(self, feature):
        count = 0
        for obj in self._dataFile:
            if obj[feature] is not None:
                count += 1
        return count

    def mean(self, feature):
        self.check_if_number(feature, "mean")
        sum = self.sum(feature)
        count = self.count(feature)
        mean = sum / count
        return mean

    def check_if_number(self, feature, func):
        if self._metaFile[feature] == 'string':
            raise Exception("Sorry, cannot "+func+ " a string for "+feature)

    def min(self, feature):
        self.check_if_number(feature, "min")
        min_value = self._dataFile[0][feature]
        for obj in self._dataFile:
            if obj[feature] is not None:
                current_num = float(obj[feature])
                if min_value is None:
                    min_value = current_num
                if min_value > current_num:
                    min_value = current_num
        return min

    def max(self, feature):
        self.check_if_number(feature, "max")
        max_value = self._dataFile[0][feature]
        for obj in self._dataFile:
            if obj[feature] is not None:
                current_num = float(obj[feature])
                if max_value is None:
                    max_value = current_num
                if max_value < current_num:
                    max_value = current_num
        return max

    def unique(self, feature):  # i will use the set data structure since it does not have duplicates
        set_values = set()
        for obj in self._dataFile:
            if obj[feature] is not None:
                set_values.add(obj[feature])
        list_features = list(set_values)
        return list_features

    def list_values(self, feature):  # including None
        list_values = []
        for obj in self._dataFile:
            list_values.append(obj[feature])
        return list_values

    def mode(self, feature):
        seen = set()  # set is better than lists for this;
        mode = None
        mode_count = 0
        values_of_feature = self.list_values(feature)
        if None in values_of_feature:
            values_of_feature.remove(None)
        for i in values_of_feature:  # the original list
            if i in seen:
                continue
            seen.add(i)
            i_count = values_of_feature.count(i)
            if i_count > mode_count:
                mode = i
                mode_count = i_count
        return mode  # will return None for an empty array

    def empty(self, feature):
        values = self.list_values(feature)
        return values.count(None)

    def to_csv(self, filename):
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=self._features)
            writer.writeheader()
            for rows in self._dataFile:
                writer.writerow(rows)

    def __getitem__(self, key):
        return self.list_values(key) if type(key) is str else self.list_values(self._features[key])

    try:
        def __init__(self, datafile, metafile):
            with open(metafile, 'r') as file_csv:
                csv_dict = csv.DictReader(file_csv)
                dictobj = next(csv_dict)
                features = []
                for feature in dictobj:
                    features.append(feature)
                with open(datafile) as file_json:
                    data = json.load(file_json)
                    self._dataFile = data["data"]
                    for data_feature in self._dataFile:
                        features_of_current_obj = data_feature.keys()
                        for element in features:  # adding the feature to the json obj and assigning it to NoneType
                            if element not in features_of_current_obj:
                                data_feature[element] = None
                        for key in list(
                                features_of_current_obj):  # deleting the feature from the json obj that does not exist in the csv file
                            if key not in features:
                                del data_feature[key]
                    self._metaFile = dictobj
                    self._features = features
    except Exception as e:
        print(type(e))
