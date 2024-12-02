import java.net.ServerSocket;
import java.io.IOException;
import java.net.Socket;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.Date;





public class HttpServer{
	public static void main(String[] args) throws Exception{
		final ServerSocket server = new ServerSocket(8080);
		System.out.println("Listening for connection on port 8080.......");


		//need this while loop otherwise the server will close lmao 
		while(true){
			//blocking method for client connection 
		 try (Socket client = server.accept()){

			
						//read http req from client
		   InputStreamReader isr = new InputStreamReader(client.getInputStream());
			 //browser may send multiple requests so making a buffered reader is better 

		  BufferedReader reader = new BufferedReader(isr);
			String line = reader.readLine();
			while (!line.isEmpty()){
				System.out.println(line);
				line = reader.readLine();
			}
				//prepare response
			Date today = new Date();

			String httpResponse = "HTTP/1.1 200 OK\r\n\r\n"+ today;
		
		 
			//send server response 

			client.getOutputStream().write(httpResponse.getBytes("UTF-8"));
			
			//close the socket
		 	
		 }
		

		}

		
	}
}
