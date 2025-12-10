package com.yourname.calculator

import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val num1 = findViewById<EditText>(R.id.num1)
        val num2 = findViewById<EditText>(R.id.num2)
        val resultText = findViewById<TextView>(R.id.resultText)

        val addButton = findViewById<Button>(R.id.addButton)
        val subButton = findViewById<Button>(R.id.subButton)
        val mulButton = findViewById<Button>(R.id.mulButton)
        val divButton = findViewById<Button>(R.id.divButton)

        addButton.setOnClickListener {
            val res = num1.text.toString().toDouble() + num2.text.toString().toDouble()
            resultText.text = "Result: $res"
        }

        subButton.setOnClickListener {
            val res = num1.text.toString().toDouble() - num2.text.toString().toDouble()
            resultText.text = "Result: $res"
        }

        mulButton.setOnClickListener {
            val res = num1.text.toString().toDouble() * num2.text.toString().toDouble()
            resultText.text = "Result: $res"
        }

        divButton.setOnClickListener {
            val num2Val = num2.text.toString().toDouble()
            if (num2Val != 0.0) {
                val res = num1.text.toString().toDouble() / num2Val
                resultText.text = "Result: $res"
            } else {
                resultText.text = "Error: Division by zero"
            }
        }
    }
}