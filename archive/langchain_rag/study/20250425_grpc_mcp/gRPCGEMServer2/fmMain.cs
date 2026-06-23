using Grpc.Core;
using SEMIGEM;
using System.Collections.Concurrent;


namespace gRPCGEMServer2
{
    public enum _VID : int { 
        EQP_STATUS = 1,
    }
    public partial class fmMain : Form
    {
        private Grpc.Core.Server rpcServer;
        private ConcurrentDictionary<int, string> _v = new ConcurrentDictionary<int, string>();

        public fmMain()
        {
            InitializeComponent();
            _v[(int)_VID.EQP_STATUS] = "STOP";
        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            if (rpcServer != null)
            {
                if (MessageBox.Show("gRPC server is already running. Do you want shutdown?") == DialogResult.OK)
                {
                    rpcServer?.ShutdownAsync().Wait();
                    rpcServer = null;
                    buttonStart.Text = "START";
                }
            }
            else
            {
                rpcServer = new Grpc.Core.Server
                {
                    Services = { SEMI_GEM_Service.BindService(new My_GEM_gRPC_Service()) },
                    Ports = { new ServerPort(tbIP.Text, int.Parse(tbPort.Text), ServerCredentials.Insecure) }
                };
                rpcServer.Start();
                buttonStart.Text = "STOP";
            }
        }

        private void buttonSet_Click(object sender, EventArgs e)
        {
            string status = cbEqpStatus.SelectedItem.ToString();
            Program.mainForm.SetV((int)_VID.EQP_STATUS, status);
        }

        private void fmMain_Load(object sender, EventArgs e)
        {
            cbEqpStatus.SelectedIndex = 0;
            tbIP.Text = "127.0.0.1";
            tbPort.Text = "50051";
        }

        public void DisplayTerminal(List<string> messageList)
        {
            if (InvokeRequired)
            {
                BeginInvoke(new Action(() => { DisplayTerminal(messageList); }));
            }
            else
            {
                TerminalMsg terminalMsg = new TerminalMsg();
                foreach (var msg in messageList)
                {
                    terminalMsg.MsgList.Add(msg);
                }
                terminalMsg.Show();
            }
        }

        public string GetV(int vid)
        {
            if (_v.ContainsKey(vid) == true)
            {
                return _v[vid];
            }
            return "";
        }

        public void SetV(int vid, string value)
        {
            if (_v.ContainsKey(vid) == true)
            {
                _v[vid] = value;
            }
        }
    }
}
