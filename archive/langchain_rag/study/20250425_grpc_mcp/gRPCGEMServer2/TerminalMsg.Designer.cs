namespace gRPCGEMServer2
{
    partial class TerminalMsg
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lbMsg = new ListBox();
            button1 = new Button();
            SuspendLayout();
            // 
            // lbMsg
            // 
            lbMsg.FormattingEnabled = true;
            lbMsg.ItemHeight = 15;
            lbMsg.Location = new Point(14, 29);
            lbMsg.Name = "lbMsg";
            lbMsg.Size = new Size(765, 379);
            lbMsg.TabIndex = 0;
            // 
            // button1
            // 
            button1.Location = new Point(321, 416);
            button1.Name = "button1";
            button1.Size = new Size(190, 26);
            button1.TabIndex = 1;
            button1.Text = "OK";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // TerminalMsg
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(button1);
            Controls.Add(lbMsg);
            Name = "TerminalMsg";
            Text = "TerminalMsg";
            Load += TerminalMsg_Load;
            ResumeLayout(false);
        }

        #endregion

        private ListBox lbMsg;
        private Button button1;
    }
}