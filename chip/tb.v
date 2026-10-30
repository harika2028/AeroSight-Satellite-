`timescale 1ns/1ps
module tb;
    reg clk = 0, rst = 1;
    wire beacon_tx;
    wire [7:0] packet_count;

    beacon #(.PERIOD(8)) dut (
        .clk(clk), .rst(rst),
        .beacon_tx(beacon_tx), .packet_count(packet_count)
    );

    always #5 clk = ~clk;

    initial begin
        $dumpfile("beacon.vcd");
        $dumpvars(0, tb);
        #20 rst = 0;
        #400 $finish;
    end

    always @(posedge clk)
        if (beacon_tx)
            $display("t=%0t  BEACON sent, packet #%0d", $time, packet_count);
endmodule