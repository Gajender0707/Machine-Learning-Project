import sys

def error_message_detail(error,error_detail:sys):
    _,_,tb_exc=error_detail.exc_info()
    file_name=tb_exc.tb_frame.f_code.co_filename
    lineno=tb_exc.tb_lineno
    error_name=error
    error_message=f"An Error is occured in python script in file{file_name} on the line number{lineno} and error is {error_name}"
    return error_message



class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(self,error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
    