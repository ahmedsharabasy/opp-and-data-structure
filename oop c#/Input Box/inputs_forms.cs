using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;

namespace Input_Box
{
    class inputs_forms
    {
        public static void InputBox(string title, string text, bool ispassword = false)
        {
            Form frm = new Form();
            frm.FormBorderStyle = FormBorderStyle.FixedToolWindow;
            frm.ControlBox = false;
            frm.Text = title;
            frm.Size = new Size(350, 250);
            // frm.Width = 350;
            // frm.Height = 250;
            frm.StartPosition = FormStartPosition.Manual;
            frm.Location = new Point((Screen.PrimaryScreen.Bounds.Width - frm.Width) / 2,(Screen.PrimaryScreen.Bounds.Height-frm.Height)/2);
            frm.Top = 0;
            frm.ShowDialog();

        }
    }
}
