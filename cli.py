import argparse
from app.utils import network
from app.services import scanner
from app.utils import file

ASCII_ART = """\n\n
                                      -      +####@####= .*:     -                                  
                                 -#: .:@@@@@@%%%%%%%%%%@@@@@@@@%    ..                              
                             :+.  =@@@@===.                -=+@@@%*%=:                              
                                @@@@#                            @@@..*#                            
                           -***@@%:            :%@@@#.            -@@%:                             
                             -@@@             @@@: =@@#             @@@                             
                         =+++*@@              @@=   #@#             :@@=+++-                        
                             -@@%             .@@@@@@@.             @@@                             
                           :==#@@#:             =***:             :@@%%=-                           
                          ...   :@@%#                            @@@.   :.                          
                             .-##**@@@@--:                 :-=@@@@-:#:                              
                                     .-@@@@@@%#########%@@@@@%*%    :%:                             
                                    :%#    .=#####@####=  :#.  +%:                                  
                                    \n\n
"""

def main():
    print(ASCII_ART)
    parser = argparse.ArgumentParser(description="PortOracle - Port Scanner")
    parser.add_argument("--ip", required=True, help="Target IP or hostname")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout for each port scan in seconds")
    parser.add_argument("--output", default="results.json", help="Output file for results (default: results.json)")
    
    args = parser.parse_args()

    resolved_ip = network.resolve_hostname(args.ip)
    open_ports = scanner.run_scan(resolved_ip, args.start, args.end, args.timeout)

    file.save_results(args.output, {"ip": resolved_ip, "open_ports": open_ports})
    print(f"\nScan completed. Results saved to '{args.output}'.")

if __name__ == "__main__":
    main()