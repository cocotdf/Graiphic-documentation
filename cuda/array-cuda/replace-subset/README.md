<h1>Replace Subset</h1>

<h2>Description</h2>

<p>Replaces an element or subarray in a n-dimensional array at the point you specify in index. Type : <em><strong>Polymorphic.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/f5/f511c8f4d844-replace_subset.png" alt="Replace_Subset.Png" width="264" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Tensor.Png" src="/_assets/shared-images/77/775fe37288a0-input_acc_inference.png" width="42"/></td>
      <td valign="top"><strong>array : <em>class,</em></strong> is the n-dimensional tensor in which you want to replace an element(s), row(s), column(s), or page(s).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_32.Png" src="/_assets/shared-images/05/052f6e6ea35b-input_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>array,</em></strong> specifies where the element, row, column or page is to be replaced in the table.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Tensor.Png" src="/_assets/shared-images/77/775fe37288a0-input_acc_inference.png" width="42"/></td>
      <td valign="top"><strong>new subarray : <em>class, </em></strong>the n-dimensional tensor that replaces an element, row, column, or page (same dimension as input “<strong>array</strong>“).</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Tensor.Png" src="/_assets/shared-images/7c/7cfbb5bb0789-output_tensor.png" width="42"/></td>
      <td valign="top"><strong>output array : <em>class,</em></strong> returns the n-dimensional tensor with the replaced element(s), row(s), column(s), or page(s).</td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Accelerator library to run it).</p>

<p align="center"><img src="assets/ex_replace_subset.png" alt="ex_replace_subset" width="260" /></p>
