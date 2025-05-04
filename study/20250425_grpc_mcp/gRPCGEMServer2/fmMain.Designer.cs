namespace gRPCGEMServer2
{
    partial class fmMain
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            tbIP = new TextBox();
            tbPort = new TextBox();
            buttonStart = new Button();
            label3 = new Label();
            cbEqpStatus = new ComboBox();
            buttonSet = new Button();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(42, 32);
            label1.Name = "label1";
            label1.Size = new Size(17, 15);
            label1.TabIndex = 0;
            label1.Text = "IP";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(312, 48);
            label2.Name = "label2";
            label2.Size = new Size(36, 15);
            label2.TabIndex = 1;
            label2.Text = "PORT";
            // 
            // tbIP
            // 
            tbIP.Location = new Point(80, 29);
            tbIP.Name = "tbIP";
            tbIP.Size = new Size(156, 23);
            tbIP.TabIndex = 2;
            // 
            // tbPort
            // 
            tbPort.Location = new Point(376, 48);
            tbPort.Name = "tbPort";
            tbPort.Size = new Size(156, 23);
            tbPort.TabIndex = 3;
            // 
            // buttonStart
            // 
            buttonStart.Location = new Point(571, 48);
            buttonStart.Name = "buttonStart";
            buttonStart.Size = new Size(127, 35);
            buttonStart.TabIndex = 4;
            buttonStart.Text = "Start";
            buttonStart.UseVisualStyleBackColor = true;
            buttonStart.Click += buttonStart_Click;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(57, 105);
            label3.Name = "label3";
            label3.Size = new Size(75, 15);
            label3.TabIndex = 5;
            label3.Text = "EQP STATUS";
            // 
            // cbEqpStatus
            // 
            cbEqpStatus.FormattingEnabled = true;
            cbEqpStatus.Items.AddRange(new object[] { "STOP", "RUN", "PAUSE" });
            cbEqpStatus.Location = new Point(56, 130);
            cbEqpStatus.Name = "cbEqpStatus";
            cbEqpStatus.Size = new Size(209, 23);
            cbEqpStatus.TabIndex = 6;
            // 
            // buttonSet
            // 
            buttonSet.Location = new Point(294, 130);
            buttonSet.Name = "buttonSet";
            buttonSet.Size = new Size(127, 35);
            buttonSet.TabIndex = 7;
            buttonSet.Text = "set";
            buttonSet.UseVisualStyleBackColor = true;
            buttonSet.Click += buttonSet_Click;
            // 
            // fmMain
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(buttonSet);
            Controls.Add(cbEqpStatus);
            Controls.Add(label3);
            Controls.Add(buttonStart);
            Controls.Add(tbPort);
            Controls.Add(tbIP);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "fmMain";
            Text = "Form1";
            Load += fmMain_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private TextBox tbIP;
        private TextBox tbPort;
        private Button buttonStart;
        private Label label3;
        private ComboBox cbEqpStatus;
        private Button buttonSet;
    }
}
