import os


class UnixFS:
    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
