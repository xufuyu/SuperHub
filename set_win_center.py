def set_win_center(root, curWidth='', curHight=''):
    '''
    设置窗口大小，并居中显示
    :param root:主窗体实例
    :param curWidth:窗口宽度，非必填，默认200
    :param curHight:窗口高度，非必填，默认200
    :return:无
    '''
    if not curWidth:
        '''获取窗口宽度，默认200'''
        curWidth = root.winfo_width()
    if not curHight:
        '''获取窗口高度，默认200'''
        curHight = root.winfo_height()
    # print(curWidth, curHight)

    # 获取屏幕宽度和高度
    scn_w, scn_h = root.maxsize()
    # print(scn_w, scn_h)

    # 计算中心坐标
    cen_x = (scn_w - curWidth) / 2
    cen_y = (scn_h - curHight) / 2
    # print(cen_x, cen_y)

    # 设置窗口初始大小和位置
    size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)
    root.geometry(size_xy)
