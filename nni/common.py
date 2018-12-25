from collections import namedtuple
from datetime import datetime
from io import TextIOBase
import logging
import os
import sys


def _load_env_args():
    args = {
        "platform": os.environ.get('NNI_PLATFOR'),
        "trial_job_id": os.environ.get('NNI_TRIAL_JOB_ID'),
        "log_dir": os.environ.get('NNI_LOG_DIRECTORY'),
        "role": os.environ.get('NNI_ROLE'),
    }
    return namedtuple('EnvArgs', args.keys())(**args)


env_args = _load_env_args()
