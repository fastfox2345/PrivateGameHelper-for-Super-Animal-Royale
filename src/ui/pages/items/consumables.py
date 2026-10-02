from core.qt_core import *
from widgets import LabeledSlider, AmmoButton, HLine, HealingButton, ThrowableButton
from images import IMAGES

class Consumables(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0, 0, 0, 0)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setObjectName("ScrollArea")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
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
        
        self.ammo_label = QLabel(self.content_area, text="弹药")
        self.ammo_label.setContentsMargins(0, 0, 0, 15)
        self.ammo_label.setObjectName("ItemsHeaderName")
        
        self.ammo_container = QWidget(self.content_area)
        self.ammo_container_layout = QGridLayout(self.ammo_container)
        self.ammo_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.ammo_container_layout.setContentsMargins(10, 0, 0, 0)
        self.ammo_container_layout.setSpacing(10)
        
        self.ammo_amount = LabeledSlider(
            self.ammo_container,
            Qt.Orientation.Horizontal,
            0,
            100,
            5,
            50,
            "弹药数量",
            "int"
        )
        self.small_bullets_button = AmmoButton(self, QPixmap(IMAGES["ammo_small"]), 55, 0)
        self.shells_bullets_button = AmmoButton(self, QPixmap(IMAGES["ammo_shells"]), 55, 1)
        self.big_bullets_button = AmmoButton(self, QPixmap(IMAGES["ammo_big"]), 55, 2)
        self.sniper_bullets_button = AmmoButton(self, QPixmap(IMAGES["ammo_sniper"]), 55, 3)
        self.special_bullets_button = AmmoButton(self, QPixmap(IMAGES["ammo_special"]), 55, 4)
        self.laser_bullets_button = AmmoButton(self, QPixmap(IMAGES["ammo_laser"]), 55, 5)
        
        self.ammo_container_layout.addWidget(self.ammo_amount, 0, 0, 1, 3)
        self.ammo_container_layout.addWidget(self.small_bullets_button, 1, 0)
        self.ammo_container_layout.addWidget(self.shells_bullets_button, 1, 1)
        self.ammo_container_layout.addWidget(self.big_bullets_button, 1, 2)
        self.ammo_container_layout.addWidget(self.sniper_bullets_button, 2, 0)
        self.ammo_container_layout.addWidget(self.special_bullets_button, 2, 1)
        self.ammo_container_layout.addWidget(self.laser_bullets_button, 2, 2)
        
        self.ammo_hline = HLine(self, h=self.line_height)
        self.ammo_hline.setObjectName("DivLine")
        
        self.healing_label = QLabel(self.content_area, text="回复物品")
        self.healing_label.setContentsMargins(0, 0, 0, 15)
        self.healing_label.setObjectName("ItemsHeaderName")
        
        self.healing_container = QWidget(self.content_area)
        self.healing_container_layout = QGridLayout(self.healing_container)
        self.healing_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.healing_container_layout.setContentsMargins(10, 0, 0, 0)
        self.healing_container_layout.setSpacing(10)
        
        self.juice_amount = LabeledSlider(
            self.healing_container,
            Qt.Orientation.Horizontal,
            0,
            200,
            5,
            100,
            "生命果汁数量",
            "int"
        )
        self.tape_amount = LabeledSlider(
            self.healing_container,
            Qt.Orientation.Horizontal,
            1,
            5,
            1,
            5,
            "胶带数量",
            "int"
        )
        self.juice_container = QWidget(self.healing_container)
        self.juice_container_layout = QVBoxLayout(self.juice_container)
        self.juice_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.juice_container_layout.setContentsMargins(22, 0, 0, 0)
        self.juice_button = HealingButton(self, QPixmap(IMAGES["juice"]), 100, "juice")
        self.juice_container_layout.addWidget(self.juice_button)
        
        self.tape_container = QWidget(self.healing_container)
        self.tape_container_layout = QVBoxLayout(self.tape_container)
        self.tape_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tape_container_layout.setContentsMargins(22, 0, 0, 0)
        self.tape_button = HealingButton(self, QPixmap(IMAGES["tape"]), 100, "tape")
        self.tape_container_layout.addWidget(self.tape_button)
        
        self.healing_container_layout.addWidget(self.juice_amount, 0, 0)
        self.healing_container_layout.addWidget(self.tape_amount, 0, 1)
        self.healing_container_layout.addWidget(self.juice_container, 1, 0)
        self.healing_container_layout.addWidget(self.tape_container, 1, 1)
        
        self.healing_hline = HLine(self, h=self.line_height)
        self.healing_hline.setObjectName("DivLine")
        
        self.throwables_label = QLabel(self.content_area, text="投掷物")
        self.throwables_label.setContentsMargins(0, 0, 0, 15)
        self.throwables_label.setObjectName("ItemsHeaderName")
        
        self.throwables_container = QWidget(self.content_area)
        self.throwables_container_layout = QGridLayout(self.throwables_container)
        self.throwables_container_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.throwables_container_layout.setContentsMargins(10, 0, 0, 0)
        self.throwables_container_layout.setSpacing(10)
        
        self.throwables_amount = LabeledSlider(
            self.throwables_container,
            Qt.Orientation.Horizontal,
            1,
            10,
            1,
            5,
            "投掷物数量",
            "int"
        )
        self.banana_button = ThrowableButton(self, QPixmap(IMAGES["banana_color"]), 55, "banana")
        self.grenade_button = ThrowableButton(self, QPixmap(IMAGES["grenade_color"]), 55, "nade")
        self.skunk_bomb_button = ThrowableButton(self, QPixmap(IMAGES["skunk_bomb_color"]), 55, "skunk")
        self.zipline_button = ThrowableButton(self, QPixmap(IMAGES["zipline_color"]), 55, "zip")
        self.cat_mine_button = ThrowableButton(self, QPixmap(IMAGES["cat_mine_color"]), 55, "mine")
        
        self.throwables_container_layout.addWidget(self.throwables_amount, 0, 0, 1, 3)
        self.throwables_container_layout.addWidget(self.banana_button, 1, 0)
        self.throwables_container_layout.addWidget(self.grenade_button, 1, 1)
        self.throwables_container_layout.addWidget(self.skunk_bomb_button, 1, 2)
        self.throwables_container_layout.addWidget(self.zipline_button, 1, 3)
        self.throwables_container_layout.addWidget(self.cat_mine_button, 1, 4)
        
        self.content_layout.addWidget(self.ammo_label)
        self.content_layout.addWidget(self.ammo_container)
        self.content_layout.addWidget(self.ammo_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.healing_label)
        self.content_layout.addWidget(self.healing_container)
        self.content_layout.addWidget(self.healing_hline)
        self.content_layout.addSpacing(10)
        self.content_layout.addWidget(self.throwables_label)
        self.content_layout.addWidget(self.throwables_container)