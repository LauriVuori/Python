#include <windows.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string.h>
#include <time.h>


// Store the formatted string of time in the output
void format_time(char * output){
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);

    sprintf(output, "{%.2d:%.2d:%.2d %.2d.%.2d.%.4d}", timeinfo->tm_hour, 
                                                     timeinfo->tm_min, 
                                                     timeinfo->tm_sec, 
                                                     timeinfo->tm_mday, 
                                                     timeinfo->tm_mon+1, 
                                                     timeinfo->tm_year + 1900);
}



HANDLE init_com_port(HANDLE Serial_handle, DCB * dcbSerialParams, COMMTIMEOUTS * timeouts) {
    fprintf(stderr, "Opening serial port: ");
    // Com port depends on your settings
    Serial_handle = CreateFile("\\\\.\\COM4", GENERIC_READ|GENERIC_WRITE, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (Serial_handle == INVALID_HANDLE_VALUE) {
        fprintf(stderr, "Error\n");
        return (HANDLE)-1;
    }
    else {
        fprintf(stderr, "Opening port OK\n");
    }
    // Set device parameters (115200 baud, 1 start bit, 1 stop bit, no parity)
    dcbSerialParams->DCBlength = sizeof(dcbSerialParams);
    fprintf(stderr, "Setting device parameters: ");
    if (GetCommState(Serial_handle, dcbSerialParams) == 0) {
        fprintf(stderr, "Error getting device state: ");
        CloseHandle(Serial_handle);
        return (HANDLE)-1;
    }
    else {
        fprintf(stderr, "Device parameters OK\n");
    }
 
    dcbSerialParams->BaudRate = CBR_115200; 
    dcbSerialParams->ByteSize = 8; 
    dcbSerialParams->StopBits = ONESTOPBIT; 
    dcbSerialParams->Parity = NOPARITY;
    fprintf(stderr, "Setting serial parameters: ");
    if(SetCommState(Serial_handle, dcbSerialParams) == 0) {
        fprintf(stderr, "Error setting device parameters\n");
        CloseHandle(Serial_handle);
        return (HANDLE)-1;
    }
    else {
        fprintf(stderr, "Setting serial parameters OK\n");
    }

    // Set COM port timeout settings
    timeouts->ReadIntervalTimeout = 50; 
    timeouts->ReadTotalTimeoutConstant = 50; 
    timeouts->ReadTotalTimeoutMultiplier = 10;
    timeouts->WriteTotalTimeoutConstant = 50; 
    timeouts->WriteTotalTimeoutMultiplier = 10;
    fprintf(stderr, "Setting timeouts: ");
    if(SetCommTimeouts(Serial_handle, timeouts) == 0) {
        fprintf(stderr, "Error setting timeouts\n"); 
        CloseHandle(Serial_handle); 
        return (HANDLE)-1;
    }
    else {
        fprintf(stderr, "Timeouts OK\n");
    }
    return Serial_handle;
}



int main() {
    HANDLE Serial_handle;
    int a = 15;
    void * ptr = &a;
    DCB dcbSerialParams = {0}; 
    COMMTIMEOUTS timeouts = {0};
    Serial_handle = init_com_port(Serial_handle, &dcbSerialParams, &timeouts);

    if (Serial_handle == INVALID_HANDLE_VALUE) {
        fprintf(stderr, "Error in init\n");
        return 0;
    }
    else {
        fprintf(stderr, "Init complete\n");
    }
    

    char buffer[35] = "{111}";
    // format_time(&buffer[0]);

    DWORD bytes_written, total_bytes_written = 0;
    fprintf(stderr, "Sending bytes...\n");
    if(!WriteFile(Serial_handle, buffer, strlen(buffer), &bytes_written, NULL)) {
        fprintf(stderr, "Error\n");
        CloseHandle(Serial_handle);
        return 1;
    }   
    fprintf(stderr, "\"%s\" sent, %d bytes sent\n", buffer, bytes_written); 



    fprintf(stderr, "Closing serial port...");

    if (CloseHandle(Serial_handle) == 0){
        fprintf(stderr, "Error\n"); 
        return 1;
    }
    fprintf(stderr, "OK\n");
    return 0;

}