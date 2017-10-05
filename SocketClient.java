import java.io.*;
import java.net.*;


/**
 * Write a description of class SocketClient here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class SocketClient
{
    
     final String hostName = "localhost";
     final int portNumber = 8888;
    
     private Socket socket;
     private BufferedReader in;
      
     
    public static void main (String[] args) throws Exception{
        SocketClient client = new SocketClient();
        
        for (int i = 0; i < 100; i ++){
            String value = client.readValue();
            System.out.println ("the answer is " + value);
        }
    
    }


    private void openSocket() throws Exception{
        socket = new Socket(hostName, portNumber);
        socket.setSoTimeout(10*1000);

         in = new BufferedReader(
            new InputStreamReader(socket.getInputStream()));
            
        
    }
    
    public String readValue() throws Exception{
       openSocket();
       String value =  in.readLine();
       socket.close();
       return value;
    }
    
}
