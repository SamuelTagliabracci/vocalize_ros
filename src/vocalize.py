#!/usr/bin/env python3
# Software License Agreement (BSD License)
#Vocalize String data on /vocalize to espeak-ng Text To Speech
#Action Server

import rospy

import subprocess

from std_msgs.msg import String

def callback(data):
  rospy.loginfo(rospy.get_caller_id() + 'Vocalize: %s', data.data)
  
  v_voice = rospy.get_param("/vocalize_node/voice")
  v_speed = rospy.get_param("/vocalize_node/speed")
  v_amplitude = rospy.get_param("/vocalize_node/amplitude")
  v_pitch = rospy.get_param("/vocalize_node/pitch")
  v_wordgap = rospy.get_param("/vocalize_node/wordgap")
  v_lastdata = rospy.get_param("/vocalize_node/lastdata")

  if data.data == v_lastdata:
    speech = ""

  elif data.data == "status":
    speech = "Checking System Status. Scanning... Analyzing Results. Systems Operational."

  elif data.data == "poweron":
    speech = "Greetings. I am X Ninety Nine E. Artificial Intelligence Maxtrix Cybernetic Robot Xeno. Power On. Systems Online. Awaiting orders."

  elif data.data == "selfdestruct":
    speech = "Self Destruct sequence initiated. Powering up reactor core to maximum settings. Self Destruct in Five. Four. Three. Two. One."

  elif data.data == "music":
    speech = ""
    bashCommand = "play /home/administrator/catkin_ws/src/vocalize_ros/AudioFX/ImperialMarch.mp3"
    subprocess.run(bashCommand, shell=True)

  else:
    speech = data.data

  rospy.set_param("/vocalize_node/lastdata", data.data)

  bashCommand = "echo " + speech + " | espeak-ng -v " + v_voice + " -p " + str(v_pitch) + " -a " + str(v_amplitude) + " -g " + str(v_wordgap) + " -s " + str(v_speed)
  subprocess.run(bashCommand, shell=True)

def listener():

  # In ROS, nodes are uniquely named. If two nodes with the same
  # name are launched, the previous one is kicked off. The
  # anonymous=True flag means that rospy will choose a unique
  # name for our 'listener' node so that multiple listeners can
  # run simultaneously.
  #rospy.init_node('listener', anonymous=True)
  rospy.init_node('vocalize')
  rospy.Subscriber('vocalize', String, callback, queue_size=1)
  # spin() simply keeps python from exiting until this node is stopped

  rospy.spin()

if __name__ == '__main__':
  listener()
