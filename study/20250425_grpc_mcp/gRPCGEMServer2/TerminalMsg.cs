using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace gRPCGEMServer2
{
    public partial class TerminalMsg : Form
    {
        public List<string> MsgList = null;
        public TerminalMsg()
        {
            InitializeComponent();
            MsgList = new List<string>();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void TerminalMsg_Load(object sender, EventArgs e)
        {
            foreach(var msg in MsgList)
            {
                lbMsg.Items.Add(msg);
            }
        }
    }
}
