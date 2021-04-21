using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
    public partial class Form1 : Form
    {
        int n=0;
        int d=0;
        int i=0;
        int s=0;
        public Form1()
        {
            InitializeComponent();
        }
        private void Form_Load(object sender, EventArgs e)
        {
            n = 0;
        }
        
        private void button2_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }
        

        private void button6_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            d = Convert.ToInt16(((Button)sender).Text);
            n = n * 10 + d;
            textBox1.Text = n.ToString();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            if(s != 0)
            {
                if (n != 0)
                {
                    if (i == 1)
                    {
                        s = s + n;
                    }
                    if (i == 2)
                    {
                        s = s - n;
                    }
                    if (i == 3)
                    {
                        s = s * n;
                    }
                    if (i == 4)
                    {
                        s = s / n;
                    }
                    textBox1.Clear();
                    textBox1.Text = s.ToString();
                    n = s;
                    s = 0;

                }
            }

            
        }

        private void button16_Click(object sender, EventArgs e)
        {
            i = 1;
            s = n;
            n = 0;
            textBox1.Clear();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            i = 2;
            s = n;
            n = 0;
            textBox1.Clear();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            i = 3;
            s = n;
            n = 0;
            textBox1.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            i = 4;
            s = n;
            n = 0;
            textBox1.Clear();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
            n = 0;
            d = 0;
            i = 0;
            s = 0;
        }
    }
}
