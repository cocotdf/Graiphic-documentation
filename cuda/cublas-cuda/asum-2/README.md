<h1>asum</h1>

<h2>Description</h2>

<p>This function computes the sum of the absolute values of the elements of vector x. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/25/25645e94b737-asum.png" alt="Asum.Png" width="209" /></p>

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
      <td width="64" valign="top"><img alt="Output_Single.Png" src="/_assets/shared-images/95/95831a40e0b5-out-single.png" width="42"/></td>
      <td valign="top"><strong>result : <em>float,</em></strong> the resulting index, which is 0 if n,incx is <=0.</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Accelerator library to run it).</p>

<p align="center"><img src="assets/ex_asum.png" alt="ex_asum" width="260" /></p>
