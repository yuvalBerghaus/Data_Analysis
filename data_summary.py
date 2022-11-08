# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import json


# Press the green button in the gutter to run the script.
class DataSummary:
    _dataFile = None

    def sum(self, feature):
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
        sum = self.sum(feature)
        count = self.count(feature)
        mean = sum / count

    def min(self, feature):
        min = self._dataFile[0][feature]
        for obj in self._dataFile:
            if obj[feature] is not None:
                current_num = float(obj[feature])
                if min is None:
                    min = current_num
                if min > current_num:
                    min = current_num
        print(min)
        return min

    def max(self, feature):
        max = self._dataFile[0][feature]
        for obj in self._dataFile:
            if obj[feature] is not None:
                current_num = float(obj[feature])
                if max is None:
                    max = current_num
                if max < current_num:
                    max = current_num
        print(max)
        return max

    def unique(self, feature):  # i will use the set data structure since it does not have duplicates
        set_values = set()
        for obj in self._dataFile:
            if obj[feature] is not None:
                set_values.add(obj[feature])
        list_features = list(set_values)
        return list_features

    def list_values(self, feature):
        list_values = []
        for obj in self._dataFile:
            list_values.append(obj[feature])
        return list_values

    def mode(self, feature):
        seen = set()  # set is better than lists for this; checking membership is cheaper
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

    def __getitem__(self, key):
        return self.list_values(key)
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
                    for data_feature in data["data"]:
                        features_of_current_obj = data_feature.keys()
                        for element in features:  # adding the feature to the json obj and assigning it to NoneType
                            if element not in features_of_current_obj:
                                data_feature[element] = None
                        for key in list(
                                features_of_current_obj):  # deleting the feature from the json obj that does not exist in the csv file
                            if key not in features:
                                del data_feature[key]
                    self._dataFile = data["data"]
                    with open("new.csv", "w") as f:
                        writer = csv.DictWriter(f, fieldnames=features)
                        writer.writeheader()
                        for rows in data["data"]:
                            writer.writerow(rows)
    except Exception as e:
        print(type(e))


# if __name__ == "__main__":
#     try:
#         metafile = "happiness_meta.csv"
#         datafile = "happiness.json"
#         DS_err = DataSummary(datafile, metafile)
#         DS_err.sum("Happiness Score")
#         DS_err.count("Happiness Score")
#         DS_err.mean("Happiness Score")
#         DS_err.min("Happiness Score")
#         DS_err.max("Happiness Score")
#         DS_err.unique("Region")
#         DS_err.mode("Region")
#         DS_err.empty("Happiness Score")
#     except Exception as err:
#         print("Exception: ", err)
