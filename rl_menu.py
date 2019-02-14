# PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from constants import *

class RLMenu(QWidget):

    def __init__(self, grid_world, reset_func):
        super().__init__()
        self.grid_world = grid_world
        self.reset_func = reset_func
        self.init_ui()

        # Init timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.grid_world.step)
        self.step_time = DEFAULT_STEP_TIME

    def init_ui(self):
        form = QFormLayout()
        self.setLayout(form)

        # World
        form.addRow(QLabel("<h2>World</h2>"))

        width_edit = QSpinBox()
        height_edit = QSpinBox()
        width_edit.setRange(1, MAX_TILES)
        height_edit.setRange(1, MAX_TILES)
        width_edit.setValue(DEFAULT_W)
        height_edit.setValue(DEFAULT_H)

        self.w_box = width_edit
        self.h_box = height_edit

        form.addRow(QLabel("Width"), width_edit)
        form.addRow(QLabel("Height"), height_edit)
        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset_grid)
        form.addRow(reset_button)

        place_button = QPushButton("Set Start Position")
        place_button.clicked.connect((lambda x: self.grid_world.set_placing(True)))
        form.addRow(place_button)

        episode_box = QCheckBox()
        if DEFAULT_EPISODIC:
            episode_box.setCheckState(Qt.Checked)
        episode_box.stateChanged.connect(
                (lambda s: self.grid_world.set_episodic((s == Qt.Checked))))
        form.addRow(QLabel("Episodic"), episode_box)

        df_edit = QDoubleSpinBox()
        df_edit.setRange(0.0, 1.0)
        df_edit.setSingleStep(0.1)
        df_edit.setValue(DEFAULT_DISCOUNT)
        df_edit.setDecimals(DECIMALS)
        df_edit.valueChanged.connect(self.grid_world.set_discount)
        form.addRow(QLabel("Discount Factor"), df_edit)

        # Training
        form.addRow(QLabel("<h2>Actions</h2>"))

        reset_pos_button = QPushButton("Reset Position")
        reset_pos_button.clicked.connect(self.grid_world.reset_position)
        form.addRow(reset_pos_button)

        train_box = QCheckBox()
        if DEFAULT_TRAIN:
            train_box.setCheckState(Qt.Checked)
        train_box.stateChanged.connect(
                (lambda s: self.grid_world.set_train((s == Qt.Checked))))
        form.addRow(QLabel("Train"), train_box)

        lr_edit = QDoubleSpinBox()
        lr_edit.setRange(0.0, 1.0)
        lr_edit.setSingleStep(0.1)
        lr_edit.setValue(DEFAULT_LR)
        lr_edit.setDecimals(DECIMALS)
        lr_edit.valueChanged.connect(self.grid_world.set_learning_rate)
        form.addRow(QLabel("Learning Rate"), lr_edit)

        step_edit = QSpinBox()
        step_edit.setRange(MIN_TRAIN_STEP, MAX_TRAIN_STEP)
        step_edit.setValue(DEFAULT_STEP_TIME)
        step_edit.valueChanged.connect(self.set_step_time)
        form.addRow(QLabel("Step Time (ms)"), step_edit)

        single_button = QPushButton("Take Single Step")
        single_button.clicked.connect(self.grid_world.step)
        form.addRow(single_button)

        run_button = QPushButton("Run")
        run_button.clicked.connect(self.run)
        stop_button = QPushButton("Stop")
        stop_button.setEnabled(False)
        stop_button.clicked.connect(self.stop)
        form.addRow(run_button, stop_button)

        self.run_button = run_button
        self.stop_button = stop_button

        # Exit
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(qApp.quit)
        form.addRow(exit_button)

    def set_step_time(self, time):
        self.step_time = time

    def reset_grid(self):
        width = self.w_box.value()
        height = self.h_box.value()

        self.reset_func(height, width)

    def run(self):
        self.timer.start(self.step_time)

        self.run_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop(self):
        self.timer.stop()

        self.run_button.setEnabled(True)
        self.stop_button.setEnabled(False)


