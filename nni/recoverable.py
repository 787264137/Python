import os

class Recoverable:
    """
    模型检查点的操作类
    """
    def load_checkpoint(self):
        pass

    def save_checkpoint(self):
        pass

    def get_checkpoint_path(self):
        ckp_path = os.getenv('NNI_CHECKPOINT_DIRECTORY')
        if ckp_path is not None and os.path.isdir(ckp_path):
            return ckp_path
        return None