from pymavlink import mavutil

# Start a connection listening on a UDP port
the_connection = mavutil.mavlink_connection('tcp:127.0.0.1:5762')
# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (
the_connection.target_system, the_connection.target_component))
# the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
#                                                          mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0,
#                                                          0, 0)
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                                          mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0,
                                                         0, 10)