module beacon #(parameter PERIOD = 8) (
    input  wire       clk,
    input  wire       rst,
    output reg        beacon_tx,
    output reg [7:0]  packet_count
);
    reg [15:0] timer;

    always @(posedge clk) begin
        if (rst) begin
            timer        <= 0;
            beacon_tx    <= 0;
            packet_count <= 0;
        end else begin
            beacon_tx <= 0;
            if (timer == PERIOD - 1) begin
                timer        <= 0;
                beacon_tx    <= 1;
                packet_count <= packet_count + 1;
            end else begin
                timer <= timer + 1;
            end
        end
    end
endmodule