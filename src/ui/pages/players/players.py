from core import *
from .content import Content
from images import IMAGES
from widgets import HLine, ClickableLabel, Button

class PagePlayers(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        
        self.header = QWidget(self)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(10, 0, 10, 0)
        
        self.header_name = QLabel(self.header, text="玩家")
        self.header_name.setObjectName("PlayersHeaderName")
        
        self.header_refresh = ClickableLabel(self)
        self.header_refresh.setToolTip("Refresh")
        self.header_refresh_icon = QPixmap(IMAGES["refresh"]).scaledToWidth(20, Qt.TransformationMode.SmoothTransformation)
        self.header_refresh.setPixmap(self.header_refresh_icon)
        self.header_refresh.setFixedSize(self.header_refresh_icon.width() + 9, self.header_refresh_icon.height() + 9)
        self.header_refresh.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_refresh.setContentsMargins(0, 0, 0, 0)
        self.header_refresh.clicked.connect(read_players)
        self.header_refresh.setObjectName("PlayersHeaderRefresh")
        
        self.header_layout.addWidget(self.header_name)
        self.header_layout.addWidget(self.header_refresh, alignment=Qt.AlignmentFlag.AlignRight)
        
        self.horizontal_line = HLine(self, h=2)
        self.horizontal_line.setObjectName("DivLine")
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = Content(self)
        self.scroll_area.setWidget(self.content_area)
        
        self.horizontal_line2 = HLine(self, h=2)
        self.horizontal_line2.setObjectName("DivLine")
        
        self.buttons = QWidget(self)
        self.buttons_layout = QHBoxLayout(self.buttons)
        self.buttons_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.buttons_layout.setContentsMargins(9, 9, 9, 0)
        self.buttons_layout.setSpacing(10)
        self.button_admin = Button(self.buttons, "管理员")
        self.button_god = Button(self.buttons, "无敌")
        self.button_kill = Button(self.buttons, "击杀")
        self.button_ghost = Button(self.buttons, "观战幽灵")
        self.button_kick = Button(self.buttons, "踢出")
        self.button_getpos = Button(self.buttons, "坐标")
        self.button_saw = Button(self.buttons, "S.A.W")
        self.button_rebel = Button(self.buttons, "反抗军")
        self.button_infect = Button(self.buttons, "感染")
        self.button_admin.clicked.connect(lambda: send_player_command("admin"))
        self.button_god.clicked.connect(lambda: send_player_command("god"))
        self.button_kill.clicked.connect(lambda: send_player_command("kill"))
        self.button_ghost.clicked.connect(lambda: send_player_command("ghost"))
        self.button_kick.clicked.connect(lambda: send_player_command("kick"))
        self.button_getpos.clicked.connect(lambda: send_player_command("getpos"))
        self.button_saw.clicked.connect(lambda: send_player_command("saw"))
        self.button_rebel.clicked.connect(lambda: send_player_command("rebel"))
        self.button_infect.clicked.connect(lambda: send_player_command("infect"))
        self.buttons_layout.addWidget(self.button_admin)
        self.buttons_layout.addWidget(self.button_god)
        self.buttons_layout.addWidget(self.button_kill)
        self.buttons_layout.addWidget(self.button_ghost)
        self.buttons_layout.addWidget(self.button_kick)
        self.buttons_layout.addWidget(self.button_getpos)
        self.buttons_layout.addWidget(self.button_saw)
        self.buttons_layout.addWidget(self.button_rebel)
        self.buttons_layout.addWidget(self.button_infect)
        
        self.button_admin.setToolTip(
            "赋予选中的的玩家当局游戏\"管理员\"权限，他们能够使用全部指令除了将管理员从本局游戏踢出。\n"
            "再次使用会移除其权限。"
        )
        
        self.button_god.setToolTip(
            "使选中的玩家无敌，免疫来自其他玩家的伤害。\n"
            "选择“全部”将为所有玩家开启无敌模式。"
        )
        
        self.button_kill.setToolTip(
            "杀死选中的的玩家或Bot，选择“全部”将杀死所有玩家 \n"
            "玩家从巨鹰上跳伞之后才能生效"
        )
        
        self.button_ghost.setToolTip(
            "将选中的玩家变为幽灵观战模式(不可逆)\n"
            "可以在大厅中使用，或者在死后使用。"
        )
        
        self.button_kick.setToolTip(
            "将选中的玩家踢出游戏。\n"
            "被踢出的玩家将不能再加入本局比赛。"
        )
        
        self.button_getpos.setToolTip(
            "显示选中的玩家的位置参数。"
        )
        
        self.button_saw.setToolTip(
            "在Svr模式里使选中的玩家移动到超级动物世界公司阵营。"
        )
        
        self.button_rebel.setToolTip(
            "在Svr模式里使选中的玩家移动到超级动物反抗军阵营。"
        )
        
        self.button_infect.setToolTip(
            "在行鸡走肉模式中使选中的的玩家感染。"
        )
        
        self.page_layout.addWidget(self.header)
        self.page_layout.addWidget(self.horizontal_line)
        self.page_layout.addWidget(self.scroll_area)
        self.page_layout.addWidget(self.horizontal_line2)
        self.page_layout.addWidget(self.buttons)
        