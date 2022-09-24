from mars_rover.src.mars_rover import MarsRover, MarsRoverController


class Test_Mars_Rover():

    def test_starting_output_is_0_0_N(self):
        rover = MarsRover()
        assert rover.get_position() == '0:0:N'

    def test_input_M_gives_0_1_N(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'M'
        controller.input(cmd)
        assert rover.get_position() == '0:1:N'

    def test_input_MM_gives_0_2_N(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'MM'
        controller.input(cmd)
        assert rover.get_position() == '0:2:N'

    def test_input_L_gives_0_0_W(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'L'
        controller.input(cmd)
        assert rover.get_position() == '0:0:W'

    def test_input_LL_gives_0_0_S(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'LL'
        controller.input(cmd)
        assert rover.get_position() == '0:0:S'

    def test_input_LLL_gives_0_0_E(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'LLL'
        controller.input(cmd)
        assert rover.get_position() == '0:0:E'

    def test_input_R_gives_0_0_E(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'R'
        controller.input(cmd)
        assert rover.get_position() == '0:0:E'

    def test_input_RR_gives_0_0_E(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'RR'
        controller.input(cmd)
        assert rover.get_position() == '0:0:S'

    def test_input_RRR_gives_0_0_W(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'RRR'
        controller.input(cmd)
        assert rover.get_position() == '0:0:W'

    def test_input_RM_gives_1_0_W(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'RM'
        controller.input(cmd)
        assert rover.get_position() == '1:0:E'

    def test_input_MRRM_gives_0_0_S(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'MRRM'
        controller.input(cmd)
        assert rover.get_position() == '0:0:S'

    def test_input_MRMR_gives_0_0_S(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'MRMR'
        controller.input(cmd)
        assert rover.get_position() == '1:1:S'

    def test_input_MMMMMMMMMM_wraps_around_to_0_0_N(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'MMMMMMMMMM'
        controller.input(cmd)
        assert rover.get_position() == '0:0:N'

    def test_input_RMMMMMMMMMM_wraps_around_to_0_0_E(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'RMMMMMMMMMM'
        controller.input(cmd)
        assert rover.get_position() == '0:0:E'

    def test_input_RRM_wraps_around_to_0_9_S(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'RRM'
        controller.input(cmd)
        assert rover.get_position() == '0:9:S'

    def test_input_LM_wraps_around_to_9_0_W(self):
        rover = MarsRover()
        controller = MarsRoverController(rover)
        cmd = 'LM'
        controller.input(cmd)
        assert rover.get_position() == '9:0:W'





