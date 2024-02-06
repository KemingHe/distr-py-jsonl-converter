
def reinit_file(fpath: str) -> None:
    '''
    Create file if not exist clear if does.

    :param fpath: file path string
    :type fpath: str
    '''
    assert fpath is not None, 'Err: invalid file path.'
    with open(fpath, 'w'):
        pass

