<h1>scal</h1>

<h2>Description</h2>

<p>This function scales the vector x by the scalar alpha and overwrites it with the result. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/ac/ac8aaba0688b-scal.png" alt="Scal.Png" width="209" /></p>

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
    <tr>
      <td width="64" valign="top"><img alt="Input_Single.Png" src="/_assets/shared-images/fd/fd47ddc3550b-input_single.png" width="42"/></td>
      <td valign="top"><strong>alpha : <em>float,</em></strong> scalar used for multiplication.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Tensor.Png" src="/_assets/shared-images/7c/7cfbb5bb0789-output_tensor.png" width="42"/></td>
      <td valign="top"><strong>x : <em>class, </em></strong>tensor of a vector with n elements.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Accelerator library to run it).</p>

<p align="center"><img src="assets/ex_scal.png" alt="ex_scal" width="260" /></p>
