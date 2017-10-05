import alsaaudio, struct, audioop, subprocess

 
# constants
CHANNELS    = 1
INFORMAT    = alsaaudio.PCM_FORMAT_FLOAT_LE
RATE        = 44100
FRAMESIZE   = 1024

YELLOW_THRESHOLD=3000
RED_TRESHOLD = 6000
 
# set up audio input
recorder=alsaaudio.PCM(type=alsaaudio.PCM_CAPTURE)
recorder.setchannels(CHANNELS)
recorder.setrate(RATE)
recorder.setformat(INFORMAT)
recorder.setperiodsize(FRAMESIZE)

  
  
def isGreen (level):
    if level < YELLOW_THRESHOLD :
        return True
    else :
        return False

 
def isYellow (level):
    if level >= YELLOW_THRESHOLD and level < RED_TRESHOLD :
        return True
    else :
        return False
 
def isRED (level):
    if level >= RED_TRESHOLD :
        return True
    else :
        return False 
 
def setGreen():
    print 'GREEN'
    
def setYellow():
    print 'YELLOW'
        
def setRed():
    print 'RED'
    
 
# main loop
runflag = 1
while runflag:
 
  # read data from audio input
  [length, data]=recorder.read()
  
  # floats= struct.unpack('f'*FRAMESIZE,data)
  level = audioop.max(data,2)
  
  if isGreen(level):
      setGreen()
  
  else :
      if isYellow(level):
          setYellow()
          
      else :
          if isRED (level) :
              setRed()
      
  

  
