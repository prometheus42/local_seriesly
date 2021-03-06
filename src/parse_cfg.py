#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""parses local_seriesly config file"""

import os
import sys


class ParseCFG(object):
    """Class that parses the local_serisly config file"""

    # {name: [ids...]}
    config_data_profiles = None

    def __init__(self):
        """parse config file"""

        # get the current dir
        currentdirpath = os.path.dirname(os.path.realpath(sys.argv[0]))

        self.config_data_profiles = {}

        # open the config file
        try:
            fdcfg = open(currentdirpath + '/show_id.cfg', 'r')
        except IOError:
            # kill local_seriesly
            print "Could not find config file"
            os._exit(0)

        # parse the config file
        # TODO: make this a little more robust (maybe use XML...)
        for line in fdcfg:
            line = line.replace(" ", "")
            if (line.find("#") == -1 and line.find("=") != -1):
                temp = line.split("=")
                name = temp[0]
                ids = temp[1].strip("\n").split(",")
                self.config_data_profiles.update({name: ids})

    def get_config_data(self):
        """get complete config data with profiles and ids"""
        return self.config_data_profiles

    def get_profile_names(self):
        """get a list of all profile names"""
        return self.config_data_profiles.keys()

    def get_show_ids(self):
        """get all unique show ids"""
        # filter the profile id to a list of all ids
        show_ids = []
        for batch in self.config_data_profiles.values():
            for show_id in batch:
                show_ids.append(show_id)

        # cast to set and back to eliminate redundant ids
        show_ids = list(set(show_ids))

        # sort list
        show_ids.sort()

        return show_ids
