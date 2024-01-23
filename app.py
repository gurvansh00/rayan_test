from rocketpy import Environment, SolidMotor, Rocket, Flight
from rocketpy.plots.environment_plots import _EnvironmentPlots
from rocketpy.plots.solid_motor_plots import _SolidMotorPlots
import streamlit as st
st.header("my project")
env = Environment(latitude=32.990254, longitude=-106.974998, elevation=1400)
import datetime
motor = SolidMotor(
    thrust_source="Cesaroni_M1670.eng",
    dry_mass=1.815,
    dry_inertia=(0.125, 0.125, 0.002),
    nozzle_radius=33 / 1000,
    grain_number=5,
    grain_density=1815,
    grain_outer_radius=33 / 1000,
    grain_initial_inner_radius=15 / 1000,
    grain_initial_height=120 / 1000,
    grain_separation=5 / 1000,
    grains_center_of_mass_position=0.397,
    center_of_dry_mass_position=0.317,
    nozzle_position=0,
    burn_time=3.9,
    throat_radius=11 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
if st.button("press me"):
    env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))  # Hour give in UTC time
    env.set_atmospheric_model(type="Forecast", file="GFS")
    envp = _EnvironmentPlots(env)
    motorp = _SolidMotorPlots(motor)
    motorp.draw()
    envp.info()
    st.image('info.jpg')
    st.image('motor.jpg')
