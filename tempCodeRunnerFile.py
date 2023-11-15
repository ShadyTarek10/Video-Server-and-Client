
            
        
            self.client_socket.close()
            self.clientAudio_socket.close()
        cmd='python client_1.py'
        self.client_1=subprocess.Popen(cmd,shell=True)