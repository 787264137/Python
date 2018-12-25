import logging
import nni
from .recoverable import Recoverable

_logger = logging.getLogger(__name__)


class Tuner(Recoverable):

    def generate_parameters(self, parameter_id):
        """

        :param parameter_id:
        :return: a set of trial (hyper-)parameters, as a serial object.
        """
        raise NotImplementedError('Tuner:generate_parameters not implemented')

    def generate_multiple_parameters(self, parameter_id_list):
        """

        :param parameter_id_list:
        :return: multiple sets of trial (hyper-)parameters, as a iterable of serializable object.
        """
        result = []
        for parameter_id in parameter_id_list:
            try:
                res = self.generate_parameters(parameter_id)
            except nni.