<h1>amin</h1>

<h2>Description</h2>

<p>This function finds the (smallest) index of the element of the minimum magnitude. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/55/55b6c9253c9e-amin.png" alt="Amin.Png" width="209" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Tensor.Png" src="/_assets/shared-images/77/775fe37288a0-input_acc_inference.png" width="42"/></td>
      <td valign="top"><strong>x : <em>class, </em></strong>tensor of a vector with n elements.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_32.Png" src="/_assets/shared-images/61/616a739c55d0-input_interger_32.png" width="42"/></td>
      <td valign="top"><strong>incx : <em>integer,</em></strong> stride between consecutive elements of x.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Interger_32.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>result : <em>integer,</em></strong> the resulting index, which is 0 if n,incx is <=0.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Accelerator library to run it).</p>

<p align="center"><img src="/_assets/shared-images/e5/e5553e7f6033-ex_amin.png" alt="ex_amin" width="260" /></p>
