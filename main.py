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
        print(self._dataFile)
        for obj in self._dataFile:
            if obj[feature] is not None:
                sum += float(obj[feature])
        print(sum)

    def count(self, feature):
        count = 0
        print(self._dataFile)
        for obj in self._dataFile:
            if obj[feature] is not None:
                count += 1
        print(count)

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


if __name__ == "__main__":
    try:
        metafile = "happiness_meta.csv"
        datafile = "happiness.json"
        DS_err = DataSummary(datafile, metafile)
        DS_err.sum("Happiness Score")
        DS_err.count("Happiness Score")
    except Exception as err:
        print("Exception: ", err)
