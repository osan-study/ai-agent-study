using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Grpc.Core;
using SEMIGEM;

namespace gRPCGEMServer2
{
    public class My_GEM_gRPC_Service : SEMI_GEM_Service.SEMI_GEM_ServiceBase
    {
        // selected equipment status request
        public override Task<S1F4> SelectedEquipmentStatusRequest(S1F3 request, ServerCallContext context)
        {
            // Process the request and prepare the response
            S1F4 response = new S1F4();
            foreach (var vid in request.SvidList)
            {
                string value = Program.mainForm.GetV(vid);
                response.SvList.Add(value);
            }

            return Task.FromResult(response);
        }

        // Date and Time Request
        public override Task<S2F18> DateandTimeRequest(S2F17 request, ServerCallContext constex)
        {
            S2F18 response = new S2F18();
            response.TIME = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");

            return Task.FromResult(response);
        }

        // host command
        public override Task<S2F42> HostCommandSend(S2F41 request, ServerCallContext context)
        {
            // Process the host command and prepare the response
            S2F42 response = new S2F42();

            response.HCACK = 0;
            response.CpAckInfoList.Add(new S2F42.Types.CPACKINFO { CPNAME = "CPNAME1", CPACK = 0 });
            response.CpAckInfoList.Add(new S2F42.Types.CPACKINFO { CPNAME = "CPNAME2", CPACK = 0 });
            response.CpAckInfoList.Add(new S2F42.Types.CPACKINFO { CPNAME = "CPNAME3", CPACK = 0 });
            response.CpAckInfoList.Add(new S2F42.Types.CPACKINFO { CPNAME = "CPNAME4", CPACK = 0 });

            return Task.FromResult(response);
        }
        // terminal display multiblock
        public override Task<S10F6> TerminalDisplayMultiBlock(S10F5 request, ServerCallContext context)
        {
            // Process the terminal display multiblock request and prepare the response
            Program.mainForm.DisplayTerminal(request.TEXTLIST.ToList());

            S10F6 response = new S10F6
            {
                ACKC10 = 0
            };

            return Task.FromResult(response);
        }
    }
    
}
