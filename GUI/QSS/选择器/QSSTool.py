class QSSTool:
    @staticmethod
    def setQssToObj(qssFile, obj):
        with open(qssFile, 'r', encoding='utf-8') as f:
            obj.setStyleSheet(f.read())