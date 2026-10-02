from core import *
from images import IMAGES
from widgets import HLine, Button, Popup

class General(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0, 0, 0, 0)
        self.page_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.line_height = 2
        
        self.preset_label = QLabel(self, text="预设")
        self.preset_label.setContentsMargins(0, 0, 0, 15)
        self.preset_label.setObjectName("PregameHeaderName")
        
        self.preset_name_container = QWidget(self)
        self.preset_name_layout = QVBoxLayout(self.preset_name_container)
        self.preset_name_layout.setContentsMargins(9, 0, 0, 0)
        
        self.name_label = QLabel(self, text="名字")
        self.name_label.setObjectName("PresetNameLabel")
        self.name_label.setContentsMargins(0, 0, 0, 0)
        
        self.name_edit = QLineEdit(self)
        self.name_edit.setFixedWidth(221)
        self.name_edit.setObjectName("LineEdit")
        self.name_edit.setContentsMargins(0, 0, 0, 0)
        self.name_edit.textChanged.connect(self.name_edited)
        
        self.preset_name_layout.addWidget(self.name_label)
        self.preset_name_layout.addWidget(self.name_edit)
        
        self.preset_buttons = QWidget(self)
        self.preset_buttons_layout = QHBoxLayout(self.preset_buttons)
        self.preset_buttons_layout.setContentsMargins(9, 0, 0, 9)
        self.preset_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.preset_buttons_layout.setSpacing(10)
        
        self.new_icon = QPixmap(IMAGES["save"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.new_button = Button(self.preset_buttons, " 新建", self.new_icon)
        self.new_button.clicked.connect(save_preset)
        self.preset_buttons_layout.addWidget(self.new_button)
        
        self.edit_icon = QPixmap(IMAGES["pencil"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.edit_button = Button(self.preset_buttons, " 保存", self.edit_icon)
        self.edit_button.clicked.connect(edit_preset)
        self.edit_button.setVisible(False)
        self.preset_buttons_layout.addWidget(self.edit_button)
        
        self.delete_icon = QPixmap(IMAGES["trash"]).scaledToHeight(13, Qt.TransformationMode.SmoothTransformation)
        self.delete_button = Button(self.preset_buttons, " 删除", self.delete_icon, btn_style="ButtonDelete")
        self.delete_button.setVisible(False)
        self.preset_buttons_layout.addWidget(self.delete_button)
        
        self.preset_hline = HLine(self, h=self.line_height)
        self.preset_hline.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.preset_hline.setObjectName("DivLine")
        
        self.control_buttons = QWidget(self)
        self.control_buttons_layout = QHBoxLayout(self.control_buttons)
        self.control_buttons_layout.setContentsMargins(0, 9, 9, 0)
        self.control_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.control_buttons_layout.setSpacing(10)
        
        self.restore_defaults_button = Button(self.control_buttons, "重置")
        self.restore_defaults_button.clicked.connect(lambda: glb.SIGNAL_MANAGER.presetRestored.emit(glb.PREGAME_DEFAULT_SETTINGS))
        self.control_buttons_layout.addWidget(self.restore_defaults_button)
        
        self.match_id_button = Button(self.control_buttons, "战局代码")
        self.match_id_button.clicked.connect(get_match_id)
        self.control_buttons_layout.addWidget(self.match_id_button)
        
        self.apply_button = Button(self.control_buttons, "应用")
        self.apply_button.clicked.connect(apply_settings)
        self.control_buttons_layout.addWidget(self.apply_button)
        
        self.start_button = Button(self.control_buttons, "开始")
        self.start_button.clicked.connect(start_game)
        self.control_buttons_layout.addWidget(self.start_button)
        
        self.page_layout.addWidget(self.preset_label)
        self.page_layout.addWidget(self.preset_name_container)
        self.page_layout.addSpacing(15)
        self.page_layout.addWidget(self.preset_buttons)
        self.page_layout.addWidget(self.preset_hline)
        self.page_layout.addWidget(self.control_buttons)
        
        self.confirm_popup = Popup(
            self, 
            "确认", 
            "你确定要\n删除这个预设吗？",
            300,
            150,
            Button(None, "取消", btn_style="ButtonDelete"),
            Button(None, "删除", btn_style="ButtonDefault")
        )
        
        self.confirm_popup.buttons[0].clicked.connect(self.confirm_popup.hide)
        self.confirm_popup.buttons[1].clicked.connect(delete_preset)

        self.confirm_popup.hide()
        
        self.delete_button.clicked.connect(self.open_popup)
        
        glb.SIGNAL_MANAGER.presetDeleted.connect(self.delete_settings)
        glb.SIGNAL_MANAGER.presetNameChanged.connect(self.name_changed)
        glb.SIGNAL_MANAGER.presetEdited.connect(self.edit_settings)
        glb.SIGNAL_MANAGER.presetSaved.connect(self.save_settings)
        glb.SIGNAL_MANAGER.presetRestored.connect(self.restore_defaults)
    
    def load_settings(self, settings: dict) -> None:
        self.name_edit.setText(settings["name"])
        self.edit_button.setVisible(True)
        self.delete_button.setVisible(True)
        send_notification("预设已加载！")
    
    def reset_settings(self) -> None:
        glb.PREGAME_SETTINGS["name"] = self.name_edit.text()
    
    def save_settings(self) -> None:
        self.name_edit.setText(glb.PREGAME_SETTINGS["name"])
        self.edit_button.setVisible(True)
        self.delete_button.setVisible(True)
        send_notification("新预设已保存！", "NotifSuccess")
        
    def edit_settings(self) -> None:
        send_notification("预设已编辑！", "NotifSuccess")
    
    def delete_settings(self) -> None:
        self.name_edit.setText("")
        self.edit_button.setVisible(False)
        self.delete_button.setVisible(False)
        self.confirm_popup.hide()
        send_notification("预设已删除！", "NotifWarning")
    
    def name_edited(self, new_name: str) -> None:
        glb.PREGAME_SETTINGS["name"] = new_name
        glb.SIGNAL_MANAGER.presetNameChanged.emit(new_name)
    
    def name_changed(self, new_name: str) -> None:
        self.name_edit.setText(new_name)
    
    def restore_defaults(self) -> None:
        send_notification("已恢复默认设置")
        
    def open_popup(self) -> None:
        self.confirm_popup.setGeometry(
            (self.width()-self.confirm_popup.width())/2,
            (self.height()-self.confirm_popup.height())/2,
            self.confirm_popup.width(),
            self.confirm_popup.height()
        )
        self.confirm_popup.show()