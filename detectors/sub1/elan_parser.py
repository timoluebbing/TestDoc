from pympi.Elan import Eaf


class ElanParser(Eaf):
    """
    A class for parsing ELAN files and extracting annotation data.

    Args:
        elan_file (str): The path to the ELAN file.

    Attributes:
        elan_file (str): The path to the ELAN file.

    """

    def __init__(self, elan_file):
        self.elan_file = elan_file
        super().__init__(file_path=self.elan_file)

    def get_tier_name(self):
        """
        Get the names of all tiers in the ELAN file.

        Returns:
            list: A list of tier names.

        """
        return self.get_tier_names()

    def get_full_time_interval(self):
        """
        Get the full time interval of the ELAN file.

        Returns:
            tuple: A tuple containing the start and end time of the ELAN file.

        """
        return self.get_full_time_interval()

    def get_annotation_data_between_times(self, tier, start, end):
        """
        Get the annotation data for a specific tier between the given start and end times.

        Args:
            tier (str): The name of the tier.
            start (float): The start time.
            end (float): The end time.

        Returns:
            list: A list of tuples containing the annotation data.

        """
        return self.get_annotation_data_between_times(tier, start, end)

    def create_annotation_data_between_times(self, start, end):
        """
        Create a dictionary of annotation data for all tiers between the given start and end times.

        Args:
            start (float): The start time.
            end (float): The end time.

        Returns:
            dict: A dictionary where the keys are tier names and the values are lists of annotation data.

        """
        annotation_dict = {}
        for tier in self.get_tier_name():
            annotation_dict[tier] = self.get_annotation_data_between_times(tier, start, end)
        return annotation_dict

    def get_unique_annotations(self, annotation_dict):
        """
        Get a dictionary of unique annotations for each tier.

        Args:
            annotation_dict (dict): A dictionary where the keys are tier names and the values are lists of annotation data.

        Returns:
            dict: A dictionary where the keys are tier names and the values are sets of unique annotations.

        """
        unique_annotations_dict = {}
        for tier, ann in annotation_dict.items():
            labels = [i[-1] for i in ann]
            # Split each item into separate items if there is a comma in between
            labels_cleaned = [item.split(', ') if ', ' in item else [item] for item in labels]
            flattened_labels = [item.strip() for sublist in labels_cleaned for item in sublist]
            unique_annotations_dict[tier] = set(flattened_labels)
        return unique_annotations_dict