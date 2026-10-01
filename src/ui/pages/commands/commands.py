from core.qt_core import *
from widgets import Button, HLine

class PageCommands(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(9, 9, 9, 22)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.content_area = QWidget(self)
        self.content_area.setObjectName("Content")
        self.scroll_area.setWidget(self.content_area)
        self.page_layout.addWidget(self.scroll_area)
        
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(0, 0, 9, 0)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        
        self.info_label = QLabel(self.content_area, text="信息")
        self.info_label.setContentsMargins(0, 0, 0, 15)
        self.info_label.setObjectName("ItemsHeaderName")
        
        self.info_container = QWidget(self.content_area)
        self.info_container_layout = QHBoxLayout(self.info_container)
        self.info_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.info_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.getplayers_button = Button(self.info_container, "/getplayers", w=125, command="getplayers")
        self.score_button = Button(self.info_container, "/score", w=125, command="score")
        self.getpid_button = Button(self.info_container, "/getpid", w=125, command="getpid")
        
        self.getplayers_button.setToolTip(
            "将包含所有玩家的列表复制到剪贴板。 \n"
            "执行该指令后，可粘贴到记事本中查看。\n"
            "在对局结束时，你可以用这个指令来获取玩家的统计数据。"
        )
        
        self.score_button.setToolTip(
            "将本局游戏的记分板复制到你的剪贴板中\n"
            "执行该指令后，可粘贴到记事本中查看。"
        )
        
        self.getpid_button.setToolTip(
            "显示你的玩家编号 #。"
        )
        
        self.info_container_layout.addWidget(self.getplayers_button)
        self.info_container_layout.addWidget(self.score_button)
        self.info_container_layout.addWidget(self.getpid_button)
        
        self.info_hline = HLine(self, h=self.line_height)
        self.info_hline.setObjectName("DivLine")
        
        self.environment_label = QLabel(self.content_area, text="环境")
        self.environment_label.setContentsMargins(0, 0, 0, 15)
        self.environment_label.setObjectName("ItemsHeaderName")
        
        self.environment_container = QWidget(self.content_area)
        self.environment_container_layout = QHBoxLayout(self.environment_container)
        self.environment_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.environment_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.night_button = Button(self.environment_container, "/night", w=125, command="night")
        self.rain_button = Button(self.environment_container, "/rain", w=125, command="rain")
        self.rain_off_button = Button(self.environment_container, "/rainoff", w=125, command="rainoff")
        self.gas_start_button = Button(self.environment_container, "/gasstart", w=125, command="gasstart")
        
        self.night_button.setToolTip(
            "切换成夜间模式。"
        )
        
        self.rain_button.setToolTip(
            "强制触发降雨的天气事件。"
        )
        
        self.rain_off_button.setToolTip(
            "强制结束下雨。\n"
            "如果已经在下雨则此操作无效。"
        )
        
        self.gas_start_button.setToolTip(
            "立即开始首个超级臭鼬毒气倒计时。\n"
            "（如果在大厅中使用，则巨鹰起飞时将立即开始倒计时）"
        )
        
        self.environment_container_layout.addWidget(self.night_button)
        self.environment_container_layout.addWidget(self.rain_button)
        self.environment_container_layout.addWidget(self.rain_off_button)
        self.environment_container_layout.addWidget(self.gas_start_button)
        
        self.environment_hline = HLine(self, h=self.line_height)
        self.environment_hline.setObjectName("DivLine")
        
        self.svr_label = QLabel(self.content_area, text="S.A.W. vs Rebellion")
        self.svr_label.setContentsMargins(0, 0, 0, 15)
        self.svr_label.setObjectName("ItemsHeaderName")
        
        self.svr_container = QWidget(self.content_area)
        self.svr_container_layout = QHBoxLayout(self.svr_container)
        self.svr_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.svr_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.boss_button = Button(self.svr_container, "/boss", w=125, command="boss")
        self.no_boss_button = Button(self.svr_container, "/noboss", w=125, command="noboss")
        
        self.boss_button.setToolTip(
            "生成一个超级星鼻鼹。"
        )
        
        self.no_boss_button.setToolTip(
            "启用或禁用生成巨型星鼻鼹。"
        )
        
        self.svr_container_layout.addWidget(self.boss_button)
        self.svr_container_layout.addWidget(self.no_boss_button)
        
        self.svr_hline = HLine(self, h=self.line_height)
        self.svr_hline.setObjectName("DivLine")
        
        self.mystery_label = QLabel(self.content_area, text="神秘模式")
        self.mystery_label.setContentsMargins(0, 0, 0, 15)
        self.mystery_label.setObjectName("ItemsHeaderName")
        
        self.mystery_container = QWidget(self.content_area)
        self.mystery_container_layout = QHBoxLayout(self.mystery_container)
        self.mystery_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.mystery_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.shotgun_sniper_button = Button(self.mystery_container, "霰弹与狙击", w=125, command="mystery 0")
        self.wild_west_button = Button(self.mystery_container, "日正当中", w=125, command="mystery 1")
        self.slow_bullets_button = Button(self.mystery_container, "子弹时间", w=125, command="mystery 2")
        self.bananarama_button = Button(self.mystery_container, "香蕉宴", w=125, command="mystery 3")
        self.handguns_only_button = Button(self.mystery_container, "手枪独大", w=125, command="mystery 4")
        self.fast_bullets_button = Button(self.mystery_container, "子弹超速", w=125, command="mystery 5")
        self.one_hit_kill_button = Button(self.mystery_container, "一击必杀", w=125, command="mystery 6")
        
        self.shotgun_sniper_button.setToolTip(
            "在神秘模式里更改为 \"霰弹与狙击\" 游戏模式。"
        )
        
        self.wild_west_button.setToolTip(
            "在神秘模式里更改为 \"日正当中\" 游戏模式。"
        )
        
        self.slow_bullets_button.setToolTip(
            "在神秘模式里更改为 \"子弹时间\" 游戏模式。."
        )
        
        self.bananarama_button.setToolTip(
            "在神秘模式里更改为 \"香蕉宴\" 游戏模式。"
        )
        
        self.handguns_only_button.setToolTip(
            "在神秘模式里更改为 \"手枪独大\" 游戏模式。."
        )
        
        self.fast_bullets_button.setToolTip(
            "在神秘模式里更改为 \"子弹超速\" 游戏模式。"
        )
        
        self.one_hit_kill_button.setToolTip(
            "在神秘模式里更改为 \"一击必杀\" 游戏模式。"
        )
        
        self.mystery_container_layout.addWidget(self.shotgun_sniper_button)
        self.mystery_container_layout.addWidget(self.wild_west_button)
        self.mystery_container_layout.addWidget(self.slow_bullets_button)
        self.mystery_container_layout.addWidget(self.bananarama_button)
        self.mystery_container_layout.addWidget(self.handguns_only_button)
        self.mystery_container_layout.addWidget(self.fast_bullets_button)
        self.mystery_container_layout.addWidget(self.one_hit_kill_button)
        
        self.mystery_hline = HLine(self, h=self.line_height)
        self.mystery_hline.setObjectName("DivLine")
        
        self.misc_label = QLabel(self.content_area, text="杂项")
        self.misc_label.setContentsMargins(0, 0, 0, 15)
        self.misc_label.setObjectName("ItemsHeaderName")
        
        self.misc_container = QWidget(self.content_area)
        self.misc_container_layout = QHBoxLayout(self.misc_container)
        self.misc_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.misc_container_layout.setContentsMargins(10, 0, 0, 0)
        
        self.flight_button = Button(self.misc_container, "/flight", w=125, command="flight")
        self.soccer_button = Button(self.misc_container, "/soccer", w=125, command="soccer")
        
        self.flight_button.setToolTip(
            "重新生成巨鹰的飞行路径。 \n"
            "只能在倒计时开始前使用。"
        )
        
        self.soccer_button.setToolTip(
            "生成狐狸沙滩球(单个社交中心只能存在一个狐狸沙滩球)。"
        )
        
        self.misc_container_layout.addWidget(self.flight_button)
        self.misc_container_layout.addWidget(self.soccer_button)
        
        self.content_layout.addWidget(self.info_label)
        self.content_layout.addWidget(self.info_container)
        self.content_layout.addWidget(self.info_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.environment_label)
        self.content_layout.addWidget(self.environment_container)
        self.content_layout.addWidget(self.environment_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.svr_label)
        self.content_layout.addWidget(self.svr_container)
        self.content_layout.addWidget(self.svr_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.mystery_label)
        self.content_layout.addWidget(self.mystery_container)
        self.content_layout.addWidget(self.mystery_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.misc_label)
        self.content_layout.addWidget(self.misc_container)